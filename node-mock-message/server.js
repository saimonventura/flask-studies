import express from "express";
import bodyParser from "body-parser";
import Redis from "ioredis";
import md5 from "md5";

const app = express();
const port = process.env.PORT || 5000;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get("/", (req, res) => {
    res.send("It's UP");
});

app.post("/newTask", (req, res) => {
    const redis = new Redis();

    const { name, slug } = req.body;
    const when = new Date().getTime();
    const status = "pending";
    const task = { name, slug, when, status };

    redis.set(`task:${md5(slug)}`, JSON.stringify(task));

    // mock to change status
    setTimeout(() => {
        task.status = Math.random() * 10 > 6 ? "done" : "fail";
        redis.set(`task:${md5(slug)}`, JSON.stringify(task));
    }, 5000);

    res.json(task);
});

app.get("/getTask/:slug", (req, res) => {
    const redis = new Redis();

    redis.get(`task:${md5(req.params.slug)}`, (err, task) => {
        if (err) {
            res.status(500).send(err);
        }
        res.json(JSON.parse(task));
    });
});

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
