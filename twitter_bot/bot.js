var Twitter = require('twitter');
var config = require('./config.js');
var T = new Twitter(config);

// Set up your search parameters
const keywords = 'github';

var params = {
  q: keywords,
  count: 10,
  result_type: 'recent',
  lang: 'en'
}

// Initiate your search using the above paramaters
T.get('search/tweets', params, function(err, data, response) {
    try {
        for(let i = 0;i<=99;i++){
            console.log(data.statuses[i].text);
    
        }
    } catch (error) {
        
    }


})