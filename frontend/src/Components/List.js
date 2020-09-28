import React, { useEffect, useState } from 'react';
import axios from "axios";
import { ListGroup, ListGroupItem, Container } from 'react-bootstrap';

function List() {
    let [userDetails, setUserDetails] = useState([]);
    useEffect(() => {
        axios.get("/list").then(response => {
            setUserDetails(response.data)
    })
        }, []
    );
    return (
    <div>
        <div style={{padding: '0 40px'}}>
            <h2>User's Details</h2>
        </div>
        {userDetails.length !== 0 ? <ListGroup style={{ padding: '20px 60px' }}>
            {userDetails.map((users, key) => (
                <ListGroupItem key={key} style={{
                    backgroundColor: '#514949',
                    textAlign: 'left',
                    color: 'white',
                    fontSize: 20,
                    padding: 10,
                    border: '2px solid black'
                }}>
                    {users.name.toUpperCase()}
                    <Container style={{ marginTop: 10 }}>
                        <ListGroup>
                            <ListGroupItem>
                                {Object.entries(users).map((data, key) => (
                                    <Container style={{
                                        padding: '0 20px',
                                        backgroundColor: 'gray',
                                    }}>
                                        <div style={{ fontWeight: 600, textDecoration: 'underline'}}>
                                        {data[0].toUpperCase()}
                                        </div>
                                        <div style={{ padding: 5}}>
                                        {data[1]}
                                        </div>
                                    </Container>
                                ))}
                            </ListGroupItem>
                        </ListGroup>
                    </Container>
                </ListGroupItem>
            ))}
        </ListGroup>
            :
            <h4 style={{ padding: '20px 60px' }} >No User has taken the survey</h4>
        }
    </div>
);
}

export default List;