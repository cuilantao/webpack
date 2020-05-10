import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter, Switch, Route} from 'react-router-dom';
import SignInPage from './signinpage/SignInPage'
import Test from './test/Test'
class App extends Component{
  render() {
    return (
      <div>
      <BrowserRouter>
        <Switch>
          <Route exact path = "/" component = {SignInPage}></Route>
          <Route exact path = "/test" component = {Test}></Route>
        </Switch>
      </BrowserRouter>
    </div>
    )
  }
}
const container = document.getElementById("app");
render(<App />, container);