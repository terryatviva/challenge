import React, { useEffect, useState } from 'react';
import axios from "axios";
import { ListGroup, ListGroupItem } from 'react-bootstrap';

function List() {
    let [userDetails, setUsserDetails] = useState([]);
    useEffect(() => {
        axios.get("http://127.0.0.1:4000/list").then(response => {
            setUsserDetails(response.data)
    })
        }, []
    );
    return (
    <div className='App'>
        <ListGroup>
            {userDetails.map((users, key) => (
                <ListGroupItem key={key} color='dark'>
                    {users.name}
                </ListGroupItem>
            ))}
        </ListGroup>
    </div>
);
}

export default List;