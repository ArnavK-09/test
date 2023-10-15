// export default class SellPassManager {
//     constructor(params: any) {
//         this.token = params.token
//         this.shop = params.shop
//     }
//     public async fetch(route: string = "") {
//         return await fetch(`https://api.sellpass.io/v2/public/shops/${this.shop}/${route}`, {
//             headers: {
//                 'Authorization': "Bearer "+this.token,
//             }
//         })
//     }

//     public async shopInfo() {
//         return await this.fetch('main')
//     }
// }
