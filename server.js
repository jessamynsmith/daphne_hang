'use strict';

const express = require('express');

const app = express();
app.use(express.json());

// API Routes

app.get('/api/v1/hang/', async function(request, response) {
});

app.set('port', process.env.PORT || 5000);

app.listen(app.get('port'), '127.0.0.1', function() {
  console.log('Express server listening on port ' + app.get('port'));
});
