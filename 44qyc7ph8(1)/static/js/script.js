// Load dashboard statistics
fetch("/api/stats")
.then(response => response.json())
.then(data => {

    document.getElementById("points").innerText =
        data.points;

    document.getElementById("tasks").innerText =
        data.tasks;

    document.getElementById("challenges").innerText =
        data.challenges;
});


// Load leaderboard
fetch("/api/leaderboard")
.then(response => response.json())
.then(users => {

    let leaderboard =
        document.getElementById("leaderboard");

    users.forEach(user => {

        let li =
            document.createElement("li");

        li.innerText =
            user.name + " - " + user.points + " points";

        leaderboard.appendChild(li);
    });

});