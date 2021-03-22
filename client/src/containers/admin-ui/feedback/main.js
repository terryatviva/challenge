import React, { useEffect, useState } from 'react';
import axios from 'axios';
import FeedbackTable from './feedback-table.js';

export default function Main(){
  const [feedbacks, setFeedback]=useState([]);
  useEffect(()=>{
    axios.get('/feedback')
      .then((rs)=>{
        setFeedback(rs.data);
      })
      .catch((err)=>{  })
  },[])

  return(
    <div>
      <h3>Feedback</h3>
      <FeedbackTable feedbacks={feedbacks}/>
    </div>
  )
}