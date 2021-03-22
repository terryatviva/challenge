import React from 'react';
import { Link, Route, Switch } from "react-router-dom";

import FeedbackMain from './containers/user-ui/feedback/main.js';
import AdminFeedbackMain from './containers/admin-ui/feedback/main.js';

export default function AppRoutes(){
  return(
    <Switch>
      <Route path="/admin/feedbacks" component={AdminFeedbackMain}></Route>
      <Route path="/userfeedback" component={FeedbackMain}></Route>
    </Switch>
  )
}

