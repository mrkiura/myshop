import React, { useEffect, useState } from 'react';
import FastAPIClient from '../../client';
import config from '../../config';
import ProductTable from "../../components/ProductTable"
import DashboardHeader from "../../components/DashboardHeader";
import Footer from "../../components/Footer";
import Loader from '../../components/Loader';
import jwtDecode from "jwt-decode";
import * as moment from "moment";
import { useNavigate } from "react-router-dom";
import CartSummaryModal from "../../components/Modal/CartSummaryModal";



const client = new FastAPIClient(config);


const Home = () => {

     const [loading, setLoading] = useState(true)
     const [isLoggedIn, setIsLoggedIn] = useState(false);
     const [products, setProducts] = useState([])
     const [searchValue, setSearchValue] = useState("")
     const navigate = useNavigate()

     useEffect(() => {
          fetchProducts()
     }, [])


     const fetchProducts = (search) => {

          if (searchValue?.length <= 0 && search)
               return alert("Please Enter Search Text")

          setLoading(true)

          client.getProducts(searchValue).then((data) => {
               setLoading(false)
               setProducts(data?.results)
          });
     }

     useEffect(() => {
		const tokenString = localStorage.getItem("token");
		if (tokenString) {
			const token = JSON.parse(tokenString);
			const decodedAccessToken = jwtDecode(token.access_token);
			if (moment.unix(decodedAccessToken.exp).toDate() > new Date()) {
				setIsLoggedIn(true);
			}
		}
	}, []);

     if (!isLoggedIn) {
          navigate("/login")
     }


     if (loading)
          return <Loader />

     return (
          <>
               <section className="bg-black ">
                    <DashboardHeader />

                    <div className="container px-5 py-12 mx-auto lg:px-20">

                         <div className="flex flex-col flex-wrap pb-6 mb-12 text-white ">
                              <h1 className="mb-6 text-3xl font-medium text-white">
                                   Quality and affordable products
                              </h1>
                              <div className="container flex justify-center items-center mb-6">
                                   <div className="relative w-full max-w-xs m-auto">
                                        <input
                                             type="text"
                                             onChange={(e) => setSearchValue(e.target.value)}
                                             className={`text-teal-500 z-20 hover:text-teal-700 h-14 w-full max-w-xs m-auto pr-8 pl-5 rounded z-0 focus:shadow focus:outline-none`} placeholder="Search products..." />
                                        <div className="absolute top-2 right-2">
                                             <button onClick={() => fetchProducts(true)} className="h-10 w-20 text-white rounded bg-teal-500 hover:bg-teal-600">Search</button>
                                        </div>
                                   </div>
                              </div>
                              <div className="mainViewport">
                                   <ProductTable
                                        products={products}
                                   />
                                   <CartSummaryModal />
                              </div>
                         </div>
                    </div>
                    <Footer />
               </section>
          </>
     )
}

export default Home;