import MainNavigation from '../components/MainNavigation';
import {Link} from 'react-router-dom'

function ErrorPage() {
  return (
    <div className="app">
      <MainNavigation />
      <main>
        <div className='middle-container'>
            <p>An Error occured! Make sure the api is Logged in</p>
            <Link to='/'> Try Again </Link>
        </div>
      </main>
    </div>
  );
}

export default ErrorPage;