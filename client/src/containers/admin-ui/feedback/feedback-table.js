import React from 'react';
import { Table } from 'react-bootstrap';

export default function FeedbackTable(props){
  let { feedbacks } = props;


  function tableRows(){
    if(!feedbacks.length){
      return <tr><td colSpan="8" className="text-center">No items found</td></tr>
    }
    return feedbacks.map((item,idx)=>{
      return(
        <tr key={idx}>
          <td>{item.name}</td>
          <td>{item.birth_date}</td>
          <td>{item.email_address}</td>
          <td>{item.country}</td>
          <td>{item.city}</td>
          <td>{item.good_comment}</td>
          <td>{item.bad_comment}</td>
        </tr>
      )
    })
  }
  return(
    <Table striped bordered hover size="sm" responsive>
      <thead>
        <tr>
          <th>Name</th>
          <th>Birth date</th>
          <th>Email Address</th>
          <th>Country</th>
          <th>City</th>
          <th colSpan="2" className="text-center">Comments</th>
        </tr>
      </thead>
      <tbody>
        {tableRows()}
      </tbody>
    </Table>
  )
}