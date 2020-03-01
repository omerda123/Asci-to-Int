import React, { Component } from 'react'
import "./App.css"

export default class App extends Component {
  constructor() {
    super();
    this.state = {
        input : '',
    };
}
  render() {
    return (
      <div className="container">
        <div className='form'>
        <h1 className="input-header"> Please enter your input:</h1>
        <textarea className="text-input" placeholder= "insert input here or drag and drop file from your PC">

        </textarea>
        <button type="submit" className="submit"> Submit!</button>
        </div>
      </div>
    )
  }
}
