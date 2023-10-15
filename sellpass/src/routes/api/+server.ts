// @ts-nocheck
import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
// import SellPassManager from '$lib/shop';

class SellPassManager {
    constructor(params: { token: string, shop: string}) {
        this.token = params.token
        this.id = params.id
        this.shop = params.shop
    }
    public async fetch(route: string) {
        return await fetch("https://dev.sellpass.io" + route, {
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        })
    }

    public async shopInfo() {
        return await (await this.fetch()).json();
    }

    public async products() {
        return (await (await this.fetch(`/v2/public/shops/${this.shop}/listings`)).json()).data.listings;
    }

    public async productInfo(id: number | string) {
        return (await (await this.fetch(`/self/${this.id}/v2/products/${id}`)).json());
    }
}


const x = new SellPassManager({
    token: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU3NTAxIiwiZXhwIjoxNzAwMDY0MzY5fQ.-SElhM39HzCMkpqE5WIiKgzqwDKplYKkiPwg9frLYHI`,
    shop: "amaristoretest.sellpass.io",
    id: 57257
})

export const GET: RequestHandler = async () => {
    // shop info 
    // const a = await x.shopInfo();

    // products 
    const products = await x.products(410035);


    // return 
    // const response = b
    return json(products);
};