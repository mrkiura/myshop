import React, { useState } from "react";
import FastAPIClient from '../../client';
import config from '../../config';


const client = new FastAPIClient(config);

const CartSummaryModal = () => {
	const [cartSummary, setCartSummary] = useState({})

	const getCartSummary = () => {
		setShowModal(true)
		client.getCartSummary().then((data) => {
			setCartSummary(data)
		});
	}
	const clearCart = () => {
		setShowModal(false)
		client.clearCart().then((data) => {
			setCartSummary(data)
		});
	}

	const [showModal, setShowModal] = useState(false);
	return (
		<>
		<button
			className="transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110  bg-teal-600 cursor-pointer hover:bg-teal-700 text-white font-bold px-4 py-2 mx-auto mt-3 rounded"
			type="button"
			onClick={() => getCartSummary()}
		>
		Cart summary
		</button>
		{showModal ? (
			<>
			<div className="flex justify-center items-center overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
				<div className="relative w-auto my-6 mx-auto max-w-3xl">
					<div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
						<div className="flex items-start justify-between p-5 border-b border-solid border-gray-300 rounded-t ">
							<h3 className="text-3xl font=semibold">General Info</h3>
				<button
					className="bg-transparent border-0 text-black float-right"
					onClick={() => setShowModal(false)}
					>
					<span className="text-black opacity-7 h-6 w-6 text-xl block bg-gray-400 py-0 rounded-full">
						x
					</span>
				</button>
			</div>

			<p className="text-black text-center">{`Total number of items: ${cartSummary.item_count}`}</p>
			<p className="text-black text-center">{`Total cost: ${cartSummary.total_cost}`}</p>
			<div className="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
                  <button
                    className="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1"
                    type="button"
                    onClick={() => clearCart()}
                  >
                    Clear
                  </button>
                  <button
                    className="text-white bg-yellow-500 active:bg-yellow-700 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1"
                    type="button"
                    onClick={() => setShowModal(false)}
                  >
                    Okay
                  </button>
                </div>
			</div>
			</div>
			</div>
			</>
		) : null}
		</>
		);
};

export default CartSummaryModal;