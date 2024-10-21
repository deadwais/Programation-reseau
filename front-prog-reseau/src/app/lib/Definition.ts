
export type User ={
        id : number;
        username :string;
        email :string;
        password_hash :string;
        created_at :Date;
    }

export type Message ={
        id_sms:number;
        sender_id:number;
        receive_id:number;
        content:string;
        create_at:Date;
}

export type Groupe ={
        id_groupe:number;
        groupe_name:string;
        created_at:Date;
}

export type Groupe_membre ={
        id_groupe_membre:number;
        groupe_id:string;
        user_id:number;
}