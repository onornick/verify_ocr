require('dotenv').config();

const Client = require('@veryfi/veryfi-sdk');
// const client_ids = process.env.CLIENT_ID;
// const client_secret = process.env.CLIENT_SECRET;
// const api_key = process.env.API_KEY;
// const username = process.env.USERNAME;

const client_id ='vrfA7J8C3OPCMktlMvHLjJASaPDVk4CKimzuOhW'
const client_secret ='fWIwIRpnyHVh0a77uyCLsejKx2nh5zDUyoTNHH0EfYpJuSG6ucZTR4DSIHwnuhDbbB100JjclSmmKKsRc8LmNgAMc0xmvvCm9WYwLXYg8Y0dKy6tjwi9eCpeT4N4PJc3'
const username ='kiprotichnickson0'
const api_key='e9775f05974eb12d6159ee8e92c33fd3'

const categories = ['Grocery', 'Utilities', 'Travel'];
const file_path = 'receip.jpg';

let veryfi_client = new Client(client_id, client_secret, username, api_key);

// Correct way to pass categories as a second argument
veryfi_client.process_document(file_path, categories).then(response => {
  console.log(response);
}).catch(error => {
  console.error(error);  // Added error handling
});

