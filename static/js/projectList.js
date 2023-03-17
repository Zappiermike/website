

const username = "Zappiermike"


ReactDOM.render(<Hello />, document.querySelector('#start'));
console.log("Hello world");



// Functions
function Hello() {
    return (
      <ul>
        <li>Hi World!</li>
      </ul>
    );
  }




// Deprecated Javascript
// import { Octokit, App } from "https://cdn.skypack.dev/octokit";
// let octokit = new Octokit({
//     auth: retrieve_token()
//  });
// const github_content = await octokit.request("GET /users/{username}/repos", {
//     username: username,
// });
// function retrieve_token(){
//     const url = "/oauth_gh_token";
//     fetch(url)
//         .then(response => response.text())
//         .then(data => {
//                 return data;
//         });
// }