import { NavLink } from "react-router-dom";
// import classes from "./MainNavigation.module.css";

export default function MainNavigation() {
  return (
    <header className='app-header'>
      <nav>
        <ul>
          <li>
            {" "}
            <NavLink
              end
              to="/"
              className={({ isActive }) => (isActive ? "active" : undefined)}
            >
              Home
            </NavLink>
          </li>
          <li>
            {" "}
            <NavLink
              to="/resume"
              className={({ isActive }) => (isActive ? "active" : undefined)}
            >
              Resume
            </NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
}
