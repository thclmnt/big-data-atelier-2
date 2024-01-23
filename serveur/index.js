import express from 'express';
import dataset from './data.json' assert {type: 'json'};

const app = express();
const PORT = 3000;

app.get('/api/data', (req, res) => {
    // /api/data?page=1
    const { page } = req.query;

    if (!page) {
        res.status(400).json({ error: 'Invalid page index' })
    }

    const filteredData = paginate(
        dataset.sort((a, b) => a.last_reported - b.last_reported),
        20,
        page
    )

    res.json(filteredData);
})

const paginate = (array, size, page) => {
    return array.slice((page - 1) * size, page * size);
}

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
