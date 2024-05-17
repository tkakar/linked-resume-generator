import './App.css';
import {createBrowserRouter, RouterProvider} from 'react-router-dom';
import HomePage from './pages/Home';
import ResumePage from './pages/ResumePage'
import RootLayout from './pages/Root';
import ErrorPage from './pages/Error';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children :[
      {path: '/', index:true, element: <HomePage />,   errorElement: <ErrorPage />}, 
      {path: '/resume', element: <ResumePage />}
    ]
  },
])

export default function App() {
  
  return (
      <RouterProvider router={router}>
      </RouterProvider>
   
  );
}