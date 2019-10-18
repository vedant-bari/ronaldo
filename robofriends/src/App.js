import React , {Component}from 'react';
import {robots} from './robots';
import CardList from './CardList';
import Searchbox from './Searchbox';
import Scroll from './Scroll';
import './App.css';

class App extends Component{
  constructor(){
    super()
    this.state={
      robots : robots,
      searchfield : ""
    }
  }

  componentDidMount(){
    fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(users => this.setState({robots: users }));
  }

  OnSearchChange =(event) =>{
     this.setState({searchfield : event.target.value})
}

  render(){
    console.log(this.state.searchfield, 'searchfield');
    const filteredRobots = this.state.robots.filter(robot =>{
      return robot.name.toLowerCase().includes(this.state.searchfield.toLowerCase())
      })
    if (this.state.robots.length ===0){
      return <h2>Loading</h2>
    }
    else{
    return(

      <div className="tc">
        <h1> Robots Title </h1>
        <Searchbox searchchange={this.OnSearchChange}/>
        <Scroll>
          <CardList robots={filteredRobots}/>
        </Scroll>  
      </div>
    );
  }
  }
}
export default App;
