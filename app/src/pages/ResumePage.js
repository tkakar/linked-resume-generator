import { PDFViewer } from '@react-pdf/renderer';
import Resume from '../components/Resume'

import {useLocation, Link} from 'react-router-dom';

export default function ResumePage(){
    const location = useLocation()

    return(
        <>
            {location?.state && <PDFViewer width="100%" height="100%"><Resume  data={location.state}></Resume></PDFViewer>  }
            {
                !location.state && 
                <div className="middle-container">
                    <p> Enter a Linkedin URL <Link to='/'> here</Link></p>
                </div>  
            }
        </>
       
         
    )
}