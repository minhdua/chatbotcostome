import { Component, Injector } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ComponentBase } from '@common/componens/ComponentBase';
import { rsIProduct } from '@common/interfaces/IProduct';
import { CategoryService } from '@common/services/public/category.service';
import { ProductService } from '@common/services/public/products.service';

@Component({
  selector: 'app-edit-product',
  templateUrl: './edit-product.component.html',
  styleUrls: ['./edit-product.component.scss'],
})
export class EditProductComponent extends ComponentBase {
  productForm!: FormGroup;
  categories: any[] = [];
  colors: any[] = [];
  sizes: any[] = [];
  isImg: Boolean = true;
  previewImage: HTMLImageElement | null = null;
  globalFile: File | null = null;
  previewImageSrc?: string =
    'https://phutungnhapkhauchinhhang.com/wp-content/uploads/2020/06/default-thumbnail.jpg';
  productId: any;

  constructor(
    injector: Injector,
    private formBuilder: FormBuilder,
    private _categoryService: CategoryService,
    private _productService: ProductService,
    private _router: Router,
    private route: ActivatedRoute
  ) {
    super(injector);
    this.previewImage = document.getElementById(
      'previewImage'
    ) as HTMLImageElement | null;
  }

  ngOnInit() {
    // Initialize the productForm FormGroup here
    this.showLoading();
    this.productForm = this.formBuilder.group({
      name: ['', Validators.required],
      price: ['', Validators.required],
      quantity: ['', Validators.required],
      category: ['', Validators.required],
      color: ['', Validators.required],
      size: ['', Validators.required],
      description: ['', Validators.required],
    });

    this.productId = this.route.snapshot.paramMap.get('id');
    if (this.route.snapshot.paramMap.get('id')) {
      this.getProductDetails(+this.productId);
    }

    this.getCategories();
    this.getColors();
    this.getSizes();
  }

  getCategories() {
    this._categoryService.getCategories().subscribe(
      (res) => {
        this.categories = res.data;
        console.log('getCategories => ', res.data);
      },
      (error) => {
        console.log(error);
      }
    );
  }

  getProductDetails(id: number) {
    // call API success, after set value below
    this._productService.getProductDetails(id).subscribe(
      (productDetails: rsIProduct) => {
        this.productForm = this.formBuilder.group({
          name: [productDetails.data.name, Validators.required],
          price: [productDetails.data.price, Validators.required],
          quantity: [productDetails.data.quantity, Validators.required],
          category: [productDetails.data.category_id, Validators.required],
          color: [productDetails.data.colors, Validators.required],
          size: [productDetails.data.sizes, Validators.required],
          description: [productDetails.data.description, Validators.required],
        });
        this.previewImageSrc = productDetails.data.image_url;
        this.hideLoading();
      },
      (error) => {
        console.log(error);
        this.hideLoading();
      }
    );
  }

  getColors() {
    this._productService.getColors().subscribe(
      (res) => {
        this.colors = res.data;
        console.log('getColors => ', res.data);
      },
      (error) => {
        console.log(error);
        this.hideLoading();
      }
    );
  }

  getSizes() {
    this._productService.getSizes().subscribe(
      (res) => {
        this.sizes = res.data;
        console.log('getSizes => ', res.data);
      },
      (error) => {
        console.log(error);
      }
    );
  }

  handleFileInput(event: any) {
    const fileInput = event.target;
    this.globalFile = fileInput.files[0];
    if (this.globalFile) {
      const reader = new FileReader();
      reader.onload = (e: any) => {
        if (e.target && typeof e.target.result === 'string') {
          this.previewImageSrc = e.target.result;
        }
      };
      this.isImg = true;
      reader.readAsDataURL(this.globalFile);
    }
  }

  onSubmit() {
    this.showLoading();
    if (this.productForm) {
      const productData = {
        name: this.productForm.get('name')?.value,
        price: this.productForm.get('price')?.value,
        quantity: this.productForm.get('quantity')?.value,
        colors: this.productForm.get('color')?.value,
        sizes: this.productForm.get('size')?.value,
        category_id: this.productForm.get('category')?.value,
        description: this.productForm.get('description')?.value,
      };
      console.log('productData:', productData);
      this._productService.updateProduct(this.productId, productData).subscribe(
        (response) => {
          if (this.globalFile) {
            const formData = new FormData();
            formData.append('image', this.globalFile);
            this._productService.postImg(response.data.id, formData).subscribe(
              (response) => {
                this.hideLoading();
                this.confirmDialog
                  .success('Product added successfully.')
                  .subscribe((res) => {
                    this._router.navigate(['admin/products']);
                  });
                console.log('Img posted successfully:', response);
              },
              (error) => {
                this.hideLoading();
                console.error('Error posting img:', error);
              }
            );
          } else {
            this.hideLoading();
            this.confirmDialog
              .success('Product added successfully.')
              .subscribe((res) => {
                this._router.navigate(['admin/products']);
              });
          }
        },
        (error) => {
          this.hideLoading();
          console.error('Error posting product:', error);
        }
      );
    }
  }
}
