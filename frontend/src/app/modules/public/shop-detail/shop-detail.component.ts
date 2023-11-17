import { Component, Injector } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ComponentBase } from '@common/componens/ComponentBase';
import { IProduct, rsIProduct } from '@common/interfaces/IProduct';
import { ProductDetailsService } from '@common/services/public/productDetails.service';
@Component({
  selector: 'app-shop-detail',
  templateUrl: './shop-detail.component.html',
  styleUrls: ['./shop-detail.component.scss'],
})
export class ShopDetailComponent extends ComponentBase {
  productId!: number;
  dataLoaded: boolean = false;
  newData: IProduct = {
    sizes: [],
    colors: [],
    products_relations: [],
  };
  quantity: number = 1;
  selectedColorIndex: number | null = null;
  selectedSizeIndex: number | null = null;
  isShowBtnCart: boolean = false;
  yourColor: string = '';
  yourSize: string = '';

  constructor(
    injector: Injector,
    private route: ActivatedRoute,
    private router: Router,
    private productDetailsService: ProductDetailsService
  ) {
    super(injector);
  }

  ngOnInit(): void {
    // Simulate fetching actual data from an API or source
    // Subscribe to route params changes
    this.route.params.subscribe((params) => {
      this.productId = parseInt(
        this.route.snapshot.paramMap.get('id') || '',
        10
      );
      this.productDetailsService.getProductDetails(this.productId).subscribe(
        (productDetails: rsIProduct) => {
          this.newData = {
            id: productDetails.data.id,
            name: productDetails.data.name,
            price: productDetails.data.price,
            quantity: productDetails.data.quantity,
            category_id: productDetails.data.category_id,
            image_url: productDetails.data.image_url,
            colors: productDetails.data.colors,
            sizes: productDetails.data.sizes,
            products_relations: productDetails.data.products_relations,
            description: productDetails.data.description,
            quantityInCart: 1
          };
          // this.dataLoaded = true;
          console.log('productDetails ===> ', productDetails);
        },
        (error) => {
          // Xử lý lỗi ở đây
        },
        () => {
          this.dataLoaded = true;
        }
      );
    });
  }

  // Function to go to a different shop detail page
  goToDifferentShopDetail(newShopId: number): void {
    this.dataLoaded = false;
    this.selectedColorIndex = null;
    this.selectedSizeIndex = null;
    this.quantity = 1;
    this.router.navigate(['/shop-detail', newShopId]);
  }

  selectColor(index: number, itemColor: string) {
    if (this.selectedColorIndex === index) {
      this.selectedColorIndex = null; // Bỏ chọn nếu đã chọn rồi
      this.yourColor = '';
    } else {
      this.selectedColorIndex = index;
      this.newData.color = itemColor;
    }
  }

  selectSize(index: number, itemSize: string) {
    if (this.selectedSizeIndex === index) {
      this.selectedSizeIndex = null; // Bỏ chọn nếu đã chọn rồi
      this.yourSize = '';
    } else {
      this.selectedSizeIndex = index;
      this.newData.size = itemSize;
    }
  }

  shouldDisableButton(): boolean {
    return this.selectedSizeIndex === null || this.selectedColorIndex === null;
  }

  decrease() {
    if (this.quantity > 1) {
      this.quantity--;
      this.newData.quantityInCart = this.quantity;
      console.log('this.newData =>', this.newData);
    }
  }

  increase() {
    this.quantity++;
    console.log('====================================');
    console.log('this.quantity => ', this.quantity);
    console.log('====================================');
    this.newData.quantityInCart = this.quantity;
    console.log('this.newData =>', this.newData);
  }

  addProductToCart() {
    this.addToCart(this.newData);
    console.log('====================================');
    console.log('this.addProductToCart =>', this.newData);
    console.log('====================================');
  }
}
