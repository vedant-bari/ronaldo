import React from 'react';

const Searchbox = ({ seachfield, searchchange}) =>{
  return(
    <div className='pa'>
        <input className='pa3 ba--green bg-lightest-blue' type="search" placeholder="search box" onChange={searchchange} />
    </div>
  );
}

export default Searchbox;
