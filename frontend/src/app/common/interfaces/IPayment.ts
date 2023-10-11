export interface IPayment {
  fullname?: string;
  address?: string;
  email?: string;
  phone?: number;
  note?: string;
  status?: string;
  products?: ProductRelation[]
}

interface ProductRelation {
  name?: string;
  product_id?: number;
  quantity?: number;
  order_color?: string;
  order_size?: string;
  price?: number;
}
