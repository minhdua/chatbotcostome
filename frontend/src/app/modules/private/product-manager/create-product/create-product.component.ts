import { Component, Injector } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ComponentBase } from '@common/componens/ComponentBase';
import { ICategory } from '@common/interfaces/ICategory';
import { CategoryService } from '@common/services/public/category.service';
import { ProductService } from '@common/services/public/products.service';

@Component({
  selector: 'app-create-product',
  templateUrl: './create-product.component.html',
  styleUrls: ['./create-product.component.scss'],
})
export class CreateProductComponent extends ComponentBase {
  productForm!: FormGroup;
  categories: any[] = [];
  colors: any[] = [];
  sizes: any[] = [];
  isImg: Boolean = false;
  previewImage: HTMLImageElement | null = null;
  globalFile: File | null = null;
  previewImageSrc: string =
    'https://phutungnhapkhauchinhhang.com/wp-content/uploads/2020/06/default-thumbnail.jpg';

  constructor(
    injector: Injector,
    private formBuilder: FormBuilder,
    private _categoryService: CategoryService,
    private _productService: ProductService,
    private _router: Router
  ) {
    super(injector);
    this.previewImage = document.getElementById(
      'previewImage'
    ) as HTMLImageElement | null;
  }

  ngOnInit() {
    this.productForm = this.formBuilder.group({
      name: ['', Validators.required],
      price: ['', Validators.required],
      quantity: ['', Validators.required],
      category: ['', Validators.required],
      color: ['', Validators.required],
      size: ['', Validators.required],
      description: ['', Validators.required],
    });
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

  getColors() {
    this._productService.getColors().subscribe(
      (res) => {
        this.colors = res.data;
        console.log('getColors => ', res.data);
      },
      (error) => {
        console.log(error);
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
      this._productService.postProduct(productData).subscribe(
        (response) => {
          console.log('Product posted successfully:', response);
          const formData = new FormData();
          if (this.globalFile) {
            formData.append('image', this.globalFile);
          }
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
        },
        (error) => {
          this.hideLoading();
          console.error('Error posting product:', error);
        }
      );
    }
  }
}
