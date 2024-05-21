import { useState } from 'react';
import { FaSearch } from 'react-icons/fa';

const defaultValue = 'Enter LinkedIn URL';

const LinkedInInput = ({loadData}) => {
  const [inputValue, setInputValue] = useState(defaultValue);
  const [isValid, setIsValid] = useState('');

  const handleChange = (e) => {
    const value = e.target.value;
    const sentized = value.replace(/\s+/g, '')
    setInputValue(sentized);
    setIsValid(checkValidity(sentized))
  };

  function resetInput(){
    setInputValue('')
    setIsValid('')
  }


  function checkValidity(value){
    const regex = /^https:\/\/www\.linkedin\.com\/in\//;
    if (!regex.test(value) || !value || value === ''   )
      return false
    else return true
  }

  async function handleSubmit(){
    if(isValid)
       loadData(inputValue)
    else setIsValid(checkValidity(inputValue))
  
  }
  return (
    <>
      <div className="middle-container">
        <input className = {isValid === false ? 'invalid' : 'valid' }
          type="text"
          id="linkedinInput"
          value={inputValue}
          onFocus= {resetInput}
          onChange={handleChange}
        /> 
        <FaSearch className="search-icon" onClick={handleSubmit}/>
      </div>
      {isValid === false && <p className='invalid-message'>Invalid LinkedIn URL: Must start with https://www.linkedin.com/in/</p>}
    </>
  );
};

export default LinkedInInput;
