const Twitter = require("twitter");
const config = require("./config.js");
const T = new Twitter(config);

// Set up your search parameters
const keywords = "github";
const tweet_num = 10;
const params = {
  q: keywords,
  count: tweet_num,
  result_type: "recent",
  lang: "en",
};

// Initiate your search using the above paramaters
T.get("search/tweets", params, function (err, data, response) {
  try {
    for (let i = 0; i <= tweet_num - 1; i++) {
      console.log(data.statuses[i].text);
    }
  } catch (error) {}
});
