from churchmembers.forms import FamilyForm
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def family_info_form(request):
    family = get_object_or_404(Family, members=request.user, status=1)
    if request.method == "POST":
        form = FamilyForm(request.POST, instance=family)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('family_detail', args=(family.slug,)))
    else:
        form = FamilyForm(instance=family)
    t = 'churchmembers/update_family_info.html'
    c = {'form': form,
         'family': family,
        }
    return render_to_response(t, c, context_instance=RequestContext(request))