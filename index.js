module.exports = {
    getHomePage: (req, res) => {
        let query = "SELECT * FROM `users` ORDER BY id ASC"; // query database to get all the players

        // execute query
        db.query(query, (err, result) => {
            if (err) {
                res.redirect('/');
            }
            res.render('Home.html', {
                title: | View Users
                ,Users: result
            });
        });
    },
};