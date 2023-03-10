console.log("HELLO WORLD");

let octokit = new Octokit({ });
const username = "Zappiermike"
// const token = retrieve_token()

// await octokit.request("GET /users/{username}/repos", {
//     username: 'USERNAME',
//     headers: {
//       'X-GitHub-Api-Version': '2022-11-28'
//     }
// });

function retrieve_token(){
    const url = "/oats";
    fetch(url)
        .then(response => response.text())
        .then(data => {
           console.log("My data is: ", data); 
        });
}