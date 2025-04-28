import React, {useEffect, useState} from 'react';

function App(){
const [userData, setUserData]=useState('');
const [productData, setProductData] = useState('');
const [orderData, setOrderData]= useState('');

useEffect(()=>{
fetch('http://192.168.49.2/users')
.then(res=>res.json())
.then(data=>setUserData(data.message || JSON.stringify(data)))
.catch(err=> setUserData('Error fetching users'));

fetch('http://192.168.49.2/products')
.then(res=>res.json())
.then(data=>setProductData(data.message || JSON.stringify(data)))
.catch(err=> setProductData('Error fetching products'));

fetch('http://192.168.49.2/orders')
.then(res=>res.json())
.then(data=>setOrderData(data.message || JSON.stringify(data)))
.catch(err=> setOrderData('Error fetching orders'));

}, []);

return (
<div style={{ padding: '2rem'}}>
<h1>E-commerce dashoard</h1>
<p><strong>User service:</strong>{userData}</p>
<p><strong>Product service:</strong>{productData}</p>
<p><strong>Order service:</strong>{orderData}</p>
</div>
);
}

export default App;

