import { Component, Injector } from '@angular/core';
import { ChatbotService } from '@common/services/public/chatbot.service';
import { IQuestion } from '@common/interfaces/IQuestion';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { IConversation } from '@common/interfaces/IConversation';
import { ComponentBase } from '@common/componens/ComponentBase';

@Component({
  selector: 'app-chat-box',
  templateUrl: './chat-box.component.html',
  styleUrls: ['./chat-box.component.scss'],
})
export class ChatBoxComponent extends ComponentBase {
  constructor(
    injector: Injector,
    private _chatbotService: ChatbotService,
    private formBuilder: FormBuilder
  ) {
    super(injector);
  }

  conversations: IConversation[] = []!;
  isChat = true;

  chatForm!: FormGroup;

  ngOnInit() {
    this.chatForm = this.formBuilder.group({
      question: ['', Validators.required],
    });
    this.getHistory();
  }

  getHistory() {
    let body = {
      session_user: this.getUuid()
    };
    this.chatForm.reset();
    this.scrollSmoothToBottom();
    this._chatbotService.getChatHistory(body).subscribe(
      (res) => {
        this.conversations = res.data;
        this.scrollSmoothToBottom();
      },
      (error) => {
        this.isChat = true;
        console.log(error);
      }
    );
  }

  addChatHistory() {
    this.isChat = false;
    const message = this.chatForm.get('question')?.value;
    this.conversations.push({
      chat_response: '',
      concepts: '',
      id: 0,
      session_user: '',
      user_say: this.chatForm.get('question')?.value,
      message_type: '',
    });
    // let body = {
    //   session_user: this.getUuid(),
    //   user_say: message,
    //   concepts: message,
    // };
    this.chatForm.reset();
    this.scrollSmoothToBottom();
    this.sendQuestionByText(message, this.getUuid());
    // this._chatbotService.addHistory(body).subscribe(
    //   (res) => {
    //     this.scrollSmoothToBottom();
    //     this.sendQuestionByText(message, this.getUuid());
    //   },
    //   (error) => {
    //     this.isChat = true;
    //     console.log(error);
    //   }
    // );
  }

  sendQuestionByText(message: string, session_user: string) {
    let question: IQuestion = {
      question: message,
      session_user: session_user
    };
    this._chatbotService.sendQuestionByText(question).subscribe(
      (res) => {
        this.isChat = true;
        this.conversations[this.conversations.length - 1].chat_response = res.answer;
        this.scrollSmoothToBottom();
      },
      (error) => {
        this.isChat = true;
        console.log(error);
      }
    );
  }

  scrollSmoothToBottom() {
    setTimeout(() => {
      const element = document.querySelector('.middle');
      if (element) {
        element.scrollTop = element.scrollHeight;
      }
    }, 100);
  }

  handleFileInput(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.isChat = false;
      this.conversations.push({
        chat_response: '',
        concepts: '',
        id: 0,
        session_user: '',
        user_say: '',
        message_type: 'image',
      });
      this.scrollSmoothToBottom();
      
      // File Preview
      const reader = new FileReader();
      reader.onload = () => {
        this.conversations[this.conversations.length - 1].user_say = reader.result as string;
      }
      reader.readAsDataURL(file);

      const formData = new FormData();
      formData.append('file_image', file);
      formData.append('session_user', this.getUuid());
      this._chatbotService.sendQuestionByImage(formData).subscribe(
        (res) => {
          this.isChat = true;
          this.conversations[this.conversations.length - 1].chat_response = res.answer;
          this.scrollSmoothToBottom();
        },
        (error) => {
          this.isChat = true;
          console.log(error);
        }
      );
    }
  }
}
