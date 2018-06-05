let request = require('request');
const argv = require('yargs').argv;

let apikey = 'd3134324c6f7286c52b142a98772f494';
//default is fredericton, take input from console, flag -c
let city = argv.c || 'Fredericton';
let url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apikey}&units=metric`;

request(url, function (err, response, body){
	if(err)
	{
		console.log('error:', error);
	}
	else
	{
		let weather = JSON.parse(body);
		//console.log('body:', body);
		console.log(`It's ${weather.main.temp} degrees in ${weather.name}!`);
	}
});
