import { Outlet } from "react-router-dom"
import MainNavigation from "../components/MainNavigation"

export default function RootLayout(){
    return (
    <div className="app">
        <MainNavigation />
        <main>
            <Outlet />
        </main>
    </div>
    )
}