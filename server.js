'use strict';
const express = require('express');
const serverless = require('serverless-http');
const app = express();
const bodyParser = require('body-parser');
const router = express.Router();
app.use(bodyParser.json());
app.use('/.netlify/functions/server', router);  // path must route to lambda
app.post(' https://euhabit.netlify.app', (req, res) => {
  res.send({
    token: 'test123'
  });
});

module.exports.handler = serverless(app);