export interface IProduct {
  id?: number;
  name?: string;
  price?: number;
  quantity?: number;
  quantityInCart?: number;
  category_id?: number;
  sizes?: string[];
  colors?: string[];
  image_url?: string;
  products_relations?: ProductRelation[];
  color?: string;
  size?: string;
  description?: string;
}

interface ProductRelation {
  category_id: number;
  colors: string[];
  id: number;
  image_url: string;
  name: string;
  orders: any[];
  price: number;
  quantity: number;
  sizes: string[];
  tags: any[];
}

export interface rsIProduct {
  data: IProduct;
}
