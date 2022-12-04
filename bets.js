import axios from "axios";

const main = () => {
  const apiKey = "560746f9f61ac1524465ac9ad600b292";
  const sportKey = "upcoming"; // use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports
  const regions = "au"; //// uk | us | eu | au. Multiple can be specified if comma delimited
  const markets = "h2h"; // h2h | spreads | totals. Multiple can be specified if comma delimited
  const oddFormat = "decimal";
  const dateFormat = "iso";

  /**const fetchResults = async () => {
    try {
      const results = await axios.get(
        "https://api.the-odds-api.com/v4/sports",
        {
          params: {
            apiKey,
            regions,
            markets,
            oddFormat,
            dateFormat,
          },
        }
      );
      console.log(results.data);
      console.log(
        "Remaining requests",
        results.headers["x-requests-remaining"]
      );
    } catch (e) {
      console.log(e);
    }
  };

  const fetchNba = async () => {
    try {
      const results = await axios.get(
        "https://api.the-odds-api.com/v4/sports/basketball_nba/odds",
        {
          params: {
            apiKey,
            dateFormat,
            oddFormat,
            regions,
          },
        }
      );
      console.log(results.data);
      console.log(
        "Remaining requests",
        results.headers["x-requests-remaining"]
      );
    } catch (e) {
      console.log(e);
    }
  };*/

  /**
   * Makes a request to the odds api & logs the results
   * @param {String} endpoint endpoint for api
   * @param {Object} params parameters for api request
   * @returns
   */
  const makeRequest = async (endpoint = "", params = { apiKey }) => {
    try {
      const results = await axios.get(
        `https://api.the-odds-api.com/v4/sports${endpoint}`,
        { params }
      );
      console.log(results);
      console.log(
        "Remaining requests",
        results.headers["x-requests-remaining"]
      );

      return results;
    } catch (e) {
      console.log(e);
    }
  };

  makeRequest();
};

main();
