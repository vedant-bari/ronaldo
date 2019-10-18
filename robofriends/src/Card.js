import React from 'react'

const Card = ({name, email, id }) =>{
  // const {name, email, id } = props
  return(
    <div className='tc grow bg-light-green dib br3 pa3 ma3 bw2 shadow-5'>
        <img src={`https://robohash.org/${id}?200x200`} alt="testingimage"></img>
        <div>
        <h2>{name}</h2>
        <h2>{email}</h2>
        </div>
    </div>
  );
}

export default Card;
