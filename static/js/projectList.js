const root = ReactDOM.createRoot(document.getElementById("root"));
let list = [];

function getRepoList(){
    const response = fetch("/github_repositories")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        list = data.promise
    })
}

function RepoCardRow(props) {
    getRepoList()
    return (
        <div className="Container">
            <div className="row">
                <div className="col-sm-6">
                    <div className="card">
                    <div className="card-body">
                        <h5 className="card-title">Special title treatment</h5>
                        <p className="card-text">With supporting text below as a natural lead-in to additional content.</p>
                        <a href="#" className="btn btn-primary">Go somewhere</a>
                    </div>
                    </div>
                </div>
                <div className="col-sm-6">
                    <div className="card">
                    <div className="card-body">
                        <h5 className="card-title">Special title treatment</h5>
                        <p className="card-text">With supporting text below as a natural lead-in to additional content.</p>
                        <a href="#" className="btn btn-primary">Go somewhere</a>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

root.render(<RepoCardRow/>);