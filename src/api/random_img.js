import axios from 'axios';


const randomImg = axios.create(
    {
        baseUrl:"http://127.0.0.1:5000/",
        timeout: 5000,
    }
)

export default randomImg;