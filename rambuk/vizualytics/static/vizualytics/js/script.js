console.log("JS loaded")
//var danishCities = JSON.parse("dk.json");
let map;
let geocoder;
let markers = [];
let totalJobs = 0;
let numberOfCities = 0;

async function search_jobs() {
    var req = new XMLHttpRequest()
        req.onreadystatechange = async function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    //error handling code here
                }
                else
                {
                    // Here we get the response
                    var response = JSON.parse(req.responseText)
                    for (const [cityName, amountOfJobs] of Object.entries(response.ajax_results)) {
                        //console.log(`The key is: ${key}: And the value is: ${value}`);
                        // Now I need to get the latitude and longditude for each city (key).. how?
                        /*
                        var city = dkCities.find(item => item.city === key)
                        pos = {lat: Number(city.lat), lng: Number(city.lng)}
                        addMarker(pos)
                        */
                        numberOfCities += 1;
                        totalJobs += amountOfJobs
                    }
                    console.log(`The job average is: ${totalJobs / numberOfCities}`)
                    // Acces key (city name), value (amount of jobs) pair in the ajax response. I recieve city names and amount of jobs in that city.
                    for (const [cityName, amountOfJobs] of Object.entries(response.ajax_results)) {
                        //console.log(`The key is: ${key}: And the value is: ${value}`);
                        // Now I need to get the latitude and longditude for each city (key).. how?
                        /*
                        var city = dkCities.find(item => item.city === key)
                        pos = {lat: Number(city.lat), lng: Number(city.lng)}
                        addMarker(pos)
                        */
                        await sleep(1)
                        jobAverage = totalJobs / numberOfCities
                        jobsComparedToAverage = amountOfJobs/jobAverage
                        console.log(`${cityName}: ${jobAverage} :: ${amountOfJobs} out of ${totalJobs}`)
                        var stringNumber = "" + amountOfJobs
                        codeAddress(cityName, stringNumber, jobsComparedToAverage)
                    }
                    totalJobs = 0; // Reset total jobs. Unsure if its needed...
                    numberOfCities = 0;
                    console.log(response.ajax_results)
                    //document.getElementById('ajax_results').innerHTML = response.ajax_results
                    //addMarker(lat_lng)
                    
                }
            }
        }
    
        req.open('POST', '/ajax', true)
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        var search_word_pass_to_js = document.getElementById('search_key_ajax').value
        req.send("search_word=" + search_word_pass_to_js) // var postVars = 'username='+un+'&secret='+sec .... you can add more like this..
        
    return false
}



async function sleep(seconds) {
    return new Promise((resolve) => setTimeout(resolve, seconds * 1000));
}

function initMap() {
    lat_lng = {lat: 55.92849991088314, lng: 9.995379472383652}
    geocoder = new google.maps.Geocoder();
    map = new google.maps.Map(document.getElementById("map"), {
    center: lat_lng,
    zoom: 7,
  }); 
}



function codeAddress(cityName, number, avg) {
    geocoder.geocode( { 'address': cityName}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        // Get the results from the geocoder request and get lat long and add the marker to the map
        //console.log(results[0])
        var latitude = results[0].geometry.location.lat();
        var longitude = results[0].geometry.location.lng();
        marker_position = {lat: latitude, lng: longitude}
        addMarker(marker_position, number, avg)
      } else {
        // ====== Decode the error status ======
        // === if we were sending the requests to fast, try this one again and increase the delay
        console.log("ERROR")
        console.log(status)
        console.log(cityName)
      }
    });
  }


function addMarker(position, number, avg) {
    const svgMarker = {
        path: "M-1.547 12l6.563-6.609-1.406-1.406-5.156 5.203-2.063-2.109-1.406 1.406zM0 0q2.906 0 4.945 2.039t2.039 4.945q0 1.453-0.727 3.328t-1.758 3.516-2.039 3.070-1.711 2.273l-0.75 0.797q-0.281-0.328-0.75-0.867t-1.688-2.156-2.133-3.141-1.664-3.445-0.75-3.375q0-2.906 2.039-4.945t4.945-2.039z",
        fillColor: "blue",
        fillOpacity: 0.6,
        strokeWeight: 0,
        rotation: 0,
        scale: avg,
        anchor: new google.maps.Point(0, 20),
      };
    const marker = new google.maps.Marker({
        position,
        map,
        icon: svgMarker,
        title: number,
    });
    markers.push(marker);
}  

window.initMap = initMap;


/*
// This example uses SVG path notation to add a vector-based symbol
// as the icon for a marker. The resulting icon is a marker-shaped
// symbol with a blue fill and no border.
function initMap() {
  const center = new google.maps.LatLng(-33.712451, 150.311823);
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 9,
    center: center,
  });
  const svgMarker = {
    path: "M-1.547 12l6.563-6.609-1.406-1.406-5.156 5.203-2.063-2.109-1.406 1.406zM0 0q2.906 0 4.945 2.039t2.039 4.945q0 1.453-0.727 3.328t-1.758 3.516-2.039 3.070-1.711 2.273l-0.75 0.797q-0.281-0.328-0.75-0.867t-1.688-2.156-2.133-3.141-1.664-3.445-0.75-3.375q0-2.906 2.039-4.945t4.945-2.039z",
    fillColor: "blue",
    fillOpacity: 0.6,
    strokeWeight: 0,
    rotation: 0,
    scale: 2,
    anchor: new google.maps.Point(0, 20),
  };

  new google.maps.Marker({
    position: map.getCenter(),
    icon: svgMarker,
    map: map,
  });
}

window.initMap = initMap;
*/