const express = require('express');
const cors = require('cors')
const app = express();

app.use(cors());


app.get('/', (req, res) => res.send('Working!!!'));


app.use('/login', (req, res) => {
  res.send({
    token: 'test123'
  });
});
