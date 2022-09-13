import Product from "../Product";
import React, {useState} from "react";
import PopupModal from "../Modal/PopupModal";
import FormInput from "../FormInput/FormInput";

const ProductTable = ({products}) => {

  const [productInfoModal, setProductInfoModal] = useState(false)

    return (
      <>
        <div className="sections-list">
          {products.length && (
              products.map((product) => (
                <Product showProductInfoModal={() => setProductInfoModal(product)} key={product.id} product={product}  />
              ))
          )}
          {!products.length && (
              <p>No products found!</p>
          )}
        </div>
        {productInfoModal && <PopupModal
						modalTitle={"Product Info"}
						onCloseBtnPress={() => {
							setProductInfoModal(false);
						}}
					>
						<div className="mt-4 text-left">
							<form className="mt-5">
								<FormInput
									disabled
									type={"text"}
									name={"name"}
									label={"Name"}
									value={productInfoModal?.name}
								/>
								<FormInput
									disabled
									type={"text"}
									name={"description"}
									label={"Description"}
									value={productInfoModal?.description}
								/>
								<FormInput
									disabled
									type={"number"}
									name={"price"}
									label={"Price"}
									value={productInfoModal?.price}
								/>
							</form>
						</div>
					</PopupModal>}
      </>
    )
}

export default ProductTable;