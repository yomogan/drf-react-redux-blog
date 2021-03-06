import React, { Component } from 'react';
import { MainRoute } from './routes';
import { SideNav } from './components/SideNav';
import { Header } from './components/Header'

class App extends Component {
  render() {
    return (
      <div>
      <Header />
      <div className="container-fluid">
          <div className="row">
            <SideNav />
            <div id="root" className="col-md-9 col-xs-11 p-l-2 p-t-2">
              <MainRoute />
            </div>
          </div>
      </div>
      </div>
    );
  }
}

export default App;
