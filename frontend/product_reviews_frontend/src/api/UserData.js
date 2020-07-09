import APIFetch from '@/helpers/APIFetch';

const endpoint = '/api/userslist/';

export class UserData {
	static getUserList() {
		  return APIFetch.get(`${endpoint}`);
    }
    static readUserId(id) {
		  return APIFetch.get(`${endpoint}${id}/`);
    }
}