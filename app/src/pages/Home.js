import LinkedInInput from "../components/LinkedInInput"
import LoadingModal from "../components/LoadingModal"
import { useNavigate } from "react-router-dom"
import { useState } from "react"
import axios from 'axios'

export default function HomePage(){

    const navigate = useNavigate()
    const [isLoading, setIsLoading] = useState(false)

    async function fetchData(url){
        setIsLoading(true)
     
      try {
        const fetchURL = `http://localhost:5555/api/profile`
        const resp  = await axios({
            url: fetchURL,  
            method: 'POST',
            params: {params: url}, 
        })
        if(resp.status === 200){
            const data = await resp.data
            setIsLoading(false)
            navigate('/resume', {state:data})
        } 
        else {
          setIsLoading(false)
          navigate('/error')
        }
      }
      catch (error) {
        console.log(error)
        setIsLoading(false)
        navigate('/error')
      }
    }
    return  (
        <>
           <LinkedInInput loadData={fetchData}/>
           {isLoading && <LoadingModal/>}
        </>
    )
}