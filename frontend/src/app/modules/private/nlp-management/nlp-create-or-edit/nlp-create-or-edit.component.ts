import { Component, Injector } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { MatChipInputEvent } from '@angular/material/chips';
import { NlpService } from '@common/services/public/nlp.service';
import { INlp } from '@common/interfaces/INlp';
import { ComponentBase } from '@common/componens/ComponentBase';

@Component({
  selector: 'app-nlp-create-or-edit',
  templateUrl: './nlp-create-or-edit.component.html',
  styleUrls: ['./nlp-create-or-edit.component.scss'],
})
export class NlpCreateOrEditComponent extends ComponentBase {
  nlpDetails: INlp = {
    id: 1,
    tag: '',
    description: '',
    patterns: [],
    responses: [],
  };
  separatorKeysCodes: number[] = [ENTER, COMMA];
  id = this._route.snapshot.params['id'] || 0;
  patterns: string[] = [];
  responses: string[] = [];
  nlpForm!: FormGroup;

  constructor(
    injector: Injector,
    private _nlp: NlpService,
    private _route: ActivatedRoute,
    private formBuilder: FormBuilder
  ) {
    super(injector);
  }

  ngOnInit() {
    this.nlpForm = this.formBuilder.group({
      tag: ['', Validators.required],
      description: ['', Validators.required],
      patterns: [''],
      responses: [''],
    });
    if(this.id != 0) {
      this.getNlpDetails();
    }
  }

  getNlpDetails() {
    this.showLoading();
    this._nlp.getNlpDetails(this.id).subscribe(
      (res) => {
        this.nlpDetails = res.data;
        this.nlpForm = this.formBuilder.group({
          tag: [this.nlpDetails.tag, Validators.required],
          description: [this.nlpDetails.description, Validators.required],
          patterns: [''],
          responses: [''],
        });
        this.nlpDetails.patterns.map(item => this.patterns.push(item.pattern_text));
        this.nlpDetails.responses.map(item => this.responses.push(item.response_text));
        this.hideLoading();
      },
      (error) => {
        console.log(error);
        this.hideLoading();
      }
    );
  }

  add(event: MatChipInputEvent, type: string): void {
    const value = (event.value || '').trim();
    if (value) {
      if (type === 'pattern') {
        this.patterns.push(value);
      } else {
        this.responses.push(value);
      }
    }

    // Clear the input value
    event.chipInput!.clear();

    if (type === 'pattern') {
      this.nlpForm.get('patterns')?.setValue('');
    } else {
      this.nlpForm.get('responses')?.setValue('');
    }
  }

  remove(data: string, type: string): void {
    const index =
      type === 'pattern'
        ? this.patterns.indexOf(data)
        : this.responses.indexOf(data);

    if (index >= 0) {
      if (type === 'pattern') {
        this.patterns.splice(index, 1);
      } else {
        this.responses.splice(index, 1);
      }
    }
  }

  onSubmit() {
    this.showLoading();
    if (this.nlpForm.valid) {
      let param;
      if (+this.id === 0) {
        param = this.create();
      } else {
        param = this.edit();
      }
      this._nlp.createOrEditNlp(param).subscribe(
        (res) => {
          this.hideLoading();
          this.confirmDialog.success('Create successfully');
        },
        (error) => {
          this.hideLoading();
          console.log(error);
        }
      );
    }
  }

  create() {
    const param: INlp = {
      id: +this.id,
      tag: this.nlpForm.get('tag')?.value,
      description: this.nlpForm.get('description')?.value,
      patterns: [],
      responses: [],
    };
    this.patterns.map((item) =>
      param.patterns.push({
        id: 0,
        pattern_text: item,
        intent_id: 0,
      })
    );
    this.responses.map((item) => 
      param.responses.push({
        id: 0,
        response_text: item,
        intent_id: 0,
      })
    );
    return param;
  }

  edit() {
    const param: INlp = {
      id: +this.id,
      tag: this.nlpForm.get('tag')?.value,
      description: this.nlpForm.get('description')?.value,
      patterns: [],
      responses: [],
    };
    this.patterns.map((item) => {
      const index = this.nlpDetails.patterns.findIndex(
        (data) => data.pattern_text === item
      );
      if (index > -1) {
        param.patterns.push(this.nlpDetails.patterns[index]);
      } else {
        param.patterns.push({
          id: 0,
          pattern_text: item,
          intent_id: this.id,
        });
      }
    });
    this.responses.map((item) => {
      const index = this.nlpDetails.responses.findIndex(
        (data) => data.response_text === item
      );
      if (index > -1) {
        param.responses.push(this.nlpDetails.responses[index]);
      } else {
        param.responses.push({
          id: 0,
          response_text: item,
          intent_id: this.id,
        });
      }
    });
    return param;
  }
}
