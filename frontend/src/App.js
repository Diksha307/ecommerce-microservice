import React, { useEffect, useState } from 'react';

function App() {
  const [userData, setUserData] = useState([]);
  const [productMessage, setProductMessage] = useState('');
  const [orderMessage, setOrderMessage] = useState('');

  useEffect(() => {
    fetch('http://192.168.49.2/users/users')
      .then(res => res.json())
      .then(data => {
      console.log(data); 
      setUserData(data.users || []);
      })
      .catch(err => setUserData([{ username: "Error", email: "Fetching users" }]));

    fetch('http://192.168.49.2/products')
      .then(res => res.json())
      .then(data => setProductMessage(data.message || JSON.stringify(data)))
      .catch(err => setProductMessage('Error fetching products'));

    fetch('http://192.168.49.2/orders')
      .then(res => res.json())
      .then(data => setOrderMessage(data.message || JSON.stringify(data)))
      .catch(err => setOrderMessage('Error fetching orders'));
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>E-commerce Dashboard</h1>

      <section style={{ marginBottom: '2rem' }}>
        <h2>User Service</h2>
        <ul>
          {userData.map(user =>{
          console.log(user);
           return (
            <li key={user._id?.$oid || user.username}>
              <strong>{user.username}</strong> — {user.email}
            </li>
          );
          })}
        </ul>
      </section>

      <section style={{ marginBottom: '2rem' }}>
        <h2> Product Service</h2>
        <p>{productMessage}</p>
      </section>

      <section>
        <h2>Order Service</h2>
        <p>{orderMessage}</p>
      </section>
    </div>
  );
}

export default App;

