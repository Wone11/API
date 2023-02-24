import React, { Component } from 'react'
import reactDom             from 'react-dom'


export default class App extends Component {
  render() {
    return (
      <div>App</div>
    )
  }
}

reactDom.render(<App/>,document.getElementById('app'))
